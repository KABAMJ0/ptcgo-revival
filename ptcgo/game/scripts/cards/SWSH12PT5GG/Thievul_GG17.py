from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import trainer_effect_shield_passive
from ptcgo.game.session.passives import carrier_pokemon


def _benched_pokemon_v(entity, carrier):
    holder = carrier_pokemon(entity) if entity is not None else None
    if holder is None:
        return False
    parent = getattr(holder, "parent", None)
    return (
        bool(parent) and parent.get_attribute(AttrID.NAME) == "bench"
        and is_pokemon_v(holder.archetype_id)
    )


def _opponent_two_or_fewer_prizes(board, carrier):
    opponent = next(
        (p for p in board.player_ids if p != carrier.owning_player_id), None)
    area = board.find_player_area(opponent, "prizePile") if opponent else None
    return area is not None and len(area.children) <= 2

card = PokemonCardDef(
    guid="2080bee0-5528-589b-bd54-71b60d9f7021",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thievul.Name",
    display_name="Thievul",
    searchable_by=["Thievul", "Stage 1", "Thievul"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nickit.Name",
    family_id=827,
    abilities=[
        Ability(
            title="Baffling",
            game_text="If your opponent has 2 or fewer Prize cards remaining, whenever your opponent plays a Supporter card from their hand, prevent all effects of that card done to your Benched Pok\u00e9mon V.",
            passive=trainer_effect_shield_passive(
                protects=_benched_pokemon_v,
                condition=_opponent_two_or_fewer_prizes),
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
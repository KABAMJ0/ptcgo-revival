from ptcgo.game.card_effects.passives_common import is_in_active_spot, retreat_discount
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _own_active_while_benched(pokemon, carrier) -> bool:
    return (pokemon.owning_player_id == carrier.owning_player_id
            and is_in_active_spot(pokemon)
            and not is_in_active_spot(carrier))

card = PokemonCardDef(
    guid="9684e4d5-04b7-584b-b478-3bb3d86a3fc7",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscruel.Name",
    display_name="Toedscruel",
    searchable_by=["Toedscruel", "Stage 1", "Toedscruel"],
    subtypes=["Stage 1"],
    collector_number=89,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    family_id=948,
    abilities=[
        Ability(
            title="Secret Forest Path",
            game_text="As long as this Pok\u00e9mon is on your Bench, your Active Pok\u00e9mon's Retreat Cost is ColorlessColorless less.",
            passive=retreat_discount(2, target_pred=_own_active_while_benched),
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
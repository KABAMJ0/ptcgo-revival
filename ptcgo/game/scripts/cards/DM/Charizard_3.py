from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack

from ptcgo.game.card_effects.passives_common import team_damage_boost_passive
from ptcgo.game.data_utils import subtypes_for
from ptcgo.game.session.passives import carrier_pokemon


def _rule_box_count(calc, carrier):
    """30 more for each of THEIR Pokemon-GX and Pokemon-EX in play."""
    board = getattr(calc, "board", None)
    if board is None:
        return 0
    count = 0
    for player_id in board.player_ids:
        if player_id == getattr(carrier, "owning_player_id", None):
            continue
        for pokemon in board.pokemon_in_play(player_id):
            subtypes = subtypes_for(pokemon.archetype_id) or []
            if "GX" in subtypes or "EX" in subtypes:
                count += 1
    return 30 * count


_resolute_flame = team_damage_boost_passive(_rule_box_count, to_active_only=True)

card = PokemonCardDef(
    guid="4c75e6fc-b291-52df-aa1b-3c8d56a13dd1",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="DM",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Resolute Flame",
            game_text="This Pok\u00e9mon's attacks do 30 more damage to your opponent's Active Pok\u00e9mon for each of their Pok\u00e9mon-GX and Pok\u00e9mon-EX in play.",
            passive=_resolute_flame,
        ),
        Attack(
            title="Fiery Blast",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)
from ptcgo.game.session.passives import effective_retreat_cost
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.card_effects.trainers import team_aqua_target
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


def _power_saver_allows(board, player_id, pokemon) -> bool:
    """Power Saver: with 4 or fewer Team Aqua Pokemon in play this Pokemon
    can't attack, so every attack is withheld from the offer list.

    An ability cannot carry this guard: `Passive.blocks_attack(pokemon,
    carrier)` is read without the board, so the count is only reachable from
    an attack's offer-time `condition(board, player_id, pokemon)`."""
    in_play = sum(1 for pid in board.player_ids
                  for active in board.pokemon_in_play(pid)
                  if team_aqua_target(active))
    return in_play > 4


card = PokemonCardDef(
    guid="723cda7f-48c1-5abe-a843-987110011893",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasKyogreEX.Name",
    display_name="Team Aqua's Kyogre-EX",
    searchable_by=["Team Aqua's Kyogre-EX", "Basic", "EX", "TeamAquasKyogreEX"],
    subtypes=["Basic", "EX"],
    collector_number=6,
    set_code="TATM",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=382,
    abilities=[
        Ability(
            title="Power Saver",
            game_text="If there are 4 or fewer Team Aqua Pok\u00e9mon in play, this Pok\u00e9mon can't attack.",
            effect=unimplemented,
        ),
        Attack(
            title="Aqua Impact",
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            condition=_power_saver_allows,
            effect=damage_per(lambda c: effective_retreat_cost(c.board, c.defender), 20, base=80),
        ),
    ],
)

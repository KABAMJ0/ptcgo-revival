from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate
from ptcgo.game.card_effects.passives_common import team_damage_boost_passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities

_POLI_NAMES = ("Poliwag", "Poliwhirl", "Poliwrath")


def _poli_attacker(pokemon) -> bool:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in _POLI_NAMES


def _enthusiasm_bonus(calc, carrier) -> int:
    """+60 only while all three evolutions sit on Politoed's side of the board."""
    present = {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
               for p in calc.board.pokemon_in_play(carrier.owning_player_id)}
    return 60 if set(_POLI_NAMES) <= present else 0

card = PokemonCardDef(
    guid="2b2bfd82-ed92-56e5-a6c1-31ba9259a26c",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Politoed.Name",
    display_name="Politoed",
    searchable_by=["Politoed", "Stage 2", "Politoed"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="DP6",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Ability(
            title="Enthusiasm",
            game_text="If you have Poliwag, Poliwhirl, and Poliwrath in play, each of these Pok\u00e9mon's attacks does 60 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(_enthusiasm_bonus,
                                              attacker_pred=_poli_attacker),
        ),
        Attack(
            title="Frog Hop",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 40 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(80)),
        ),
    ],
)
from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_discard_opponent_energy, flip_gate
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="8648b342-cb51-5848-b61f-c8fad11eee15",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GroudonEX.Name",
    display_name="Groudon-EX",
    searchable_by=["Groudon-EX", "Basic", "EX", "GroudonEX"],
    subtypes=["Basic", "EX"],
    collector_number=150,
    set_code="XY5",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Rip Claw",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=composed(lambda ctx: ctx.deal_damage(), flip_gate(then=discard_opponent_energy_attack(1, damage=0))),
        ),
        Attack(
            title="Massive Rend",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
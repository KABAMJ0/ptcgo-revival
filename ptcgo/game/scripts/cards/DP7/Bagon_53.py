from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_gate
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
card = PokemonCardDef(
    guid="a406e4eb-0556-538b-b395-d084e5258f35",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bagon.Name",
    display_name="Bagon",
    searchable_by=["Bagon", "Basic", "Bagon"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="DP7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=371,
    abilities=[
        Attack(
            title="Scary Face",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack or retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_gate(discard_opponent_energy_attack(1)),
        ),
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
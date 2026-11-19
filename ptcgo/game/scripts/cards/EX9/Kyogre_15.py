from ptcgo.game.data_utils import unimplemented, unimplemented, PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_gate
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack, flip_gate
from ptcgo.game.card_effects.attacks_common import flip_attack_and_retreat_lock


card = PokemonCardDef(
    guid="c1b9b4d7-69c2-55f6-831e-27d3af543765",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic", "Kyogre"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="EX9",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Scary Face",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon can't attack or retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_attack_and_retreat_lock(),
        ),
        Attack(
            title="Hydro Pump",
            game_text="Does 40 damage plus 10 more damage for each Water Energy attached to Kyogre but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
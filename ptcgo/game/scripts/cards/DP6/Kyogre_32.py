from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, spread_damage
from ptcgo.game.card_effects.pokemon import is_basic_water_energy
from ptcgo.game.card_effects.support_common import attach_from_hand


card = PokemonCardDef(
    guid="46403c79-6dae-5bfd-afc7-46306ff2d796",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name",
    display_name="Kyogre",
    searchable_by=["Kyogre", "Basic", "Kyogre"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=382,
    abilities=[
        Attack(
            title="Drizzle",
            game_text="Choose up to 2 basic Water Energy cards from your hand and attach them to 1 of your Pok\u00e9mon.",
            cost={},
            effect=attach_from_hand(predicate=is_basic_water_energy, count=2, target="choice", minimum=0),
        ),
        Attack(
            title="High Tide",
            game_text="Discard 2 Water Energy attached to Kyogre. This attack does 20 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.WATER, also=spread_damage(20, side="opponent")),
        ),
    ],
)
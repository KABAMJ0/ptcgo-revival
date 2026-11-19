from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack, spread_damage
from ptcgo.game.card_effects.pokemon import is_basic_fighting_energy
from ptcgo.game.card_effects.support_common import attach_from_hand


card = PokemonCardDef(
    guid="7dda3882-d47d-5e6b-aa9b-b233c7e553b6",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic", "Groudon"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=383,
    abilities=[
        Attack(
            title="Drought",
            game_text="Choose up to 2 basic Fighting Energy cards from your hand and attach them to 1 of your Pok\u00e9mon.",
            cost={},
            effect=attach_from_hand(predicate=is_basic_fighting_energy, count=2, target="choice", minimum=0),
        ),
        Attack(
            title="Major Earthquake",
            game_text="Discard 2 Fighting Energy attached to Groudon and this attack does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.FIGHTING, also=spread_damage(10, side="mine")),
        ),
    ],
)
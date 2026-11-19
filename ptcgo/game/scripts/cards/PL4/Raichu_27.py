from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e6d2a8c9-5018-56c6-a10a-8f966a1052d7",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1", "Raichu"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=25,
    abilities=[
        Attack(
            title="Boosted Voltage",
            game_text="If Raichu has a Pok\u00e9mon Tool card attached to it, this attack does 20 damage to each of your opponent's Benched Pok\u00e9mon that isn't an Evolved Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Thunder Blast",
            game_text="Discard a Lightning Energy card attached to Raichu.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=self_energy_discard_attack(count=1, energy_type=PokemonTypes.LIGHTNING),
        ),
    ],
)
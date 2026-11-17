from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dac0776f-caec-5559-a3b1-71c380bc7146",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninjaex.Name",
    display_name="Greninja ex",
    searchable_by=["Greninja ex", "Stage 2", "ex", "Greninjaex"],
    subtypes=["Stage 2", "ex"],
    collector_number=54,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=658,
    abilities=[
        Attack(
            title="Stealthy Shuriken",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Torrential Slash",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
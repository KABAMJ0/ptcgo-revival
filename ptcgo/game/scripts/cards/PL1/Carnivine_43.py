from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="731aad50-335f-530a-9297-2dcbaa97c310",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic", "Carnivine"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=455,
    abilities=[
        Attack(
            title="Stretch Vine",
            game_text="Choose 2 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to each of them. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Absorb",
            game_text="Remove 2 damage counters from Carnivine.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Vine Extract",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, the Defending Pok\u00e9mon is now Burned and Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)
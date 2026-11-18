from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="76d9d9db-4b0e-5891-937c-750324af1920",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1", "Octillery"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="PL1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Attack(
            title="Water Vein",
            game_text="Reveal the top 5 cards of your deck. Flip a coin for each Energy card you find there. This attack does 50 damage times the number of heads. Shuffle the revealed cards back into your deck.",
            cost={},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Octazooka",
            game_text="Any time the Defending Pok\u00e9mon tries to attack, your opponent flips a coin. If tails, that attack does nothing. (If the Defending Pok\u00e9mon is no longer your opponent's Active Pok\u00e9mon, this effect ends.)",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)
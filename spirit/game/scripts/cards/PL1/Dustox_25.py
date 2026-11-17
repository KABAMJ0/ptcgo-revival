from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3f9b560d-79e7-58eb-bad2-1a0cd213ca60",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dustox.Name",
    display_name="Dustox",
    searchable_by=["Dustox", "Stage 2", "Dustox"],
    subtypes=["Stage 2"],
    collector_number=25,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Camouflage Pattern",
            game_text="Prevent all effects of attacks, including damage, done to Dustox by your opponent's Pok\u00e9mon that is affected by 2 or more Special Conditions.",
            effect=unimplemented,
        ),
        Attack(
            title="Smogscreen",
            game_text="The Defending Pok\u00e9mon is now Poisoned. If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Chemical Scale",
            game_text="If the Defending Pok\u00e9mon has any Pok\u00e9-Powers or Pok\u00e9-Bodies, the Defending Pok\u00e9mon is now Burned and Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
    ],
)
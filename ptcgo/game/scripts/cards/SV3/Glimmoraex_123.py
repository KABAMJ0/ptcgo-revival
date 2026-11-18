from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cff19746-31c7-5c21-a57b-686c613cef19",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmoraex.Name",
    display_name="Glimmora ex",
    searchable_by=["Glimmora ex", "Stage 1", "ex", "Glimmoraex"],
    subtypes=["Stage 1", "ex"],
    collector_number=123,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    family_id=969,
    abilities=[
        Ability(
            title="Dust Field",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your opponent can't have more than 3 Benched Pok\u00e9mon. If they have 4 or more Benched Pok\u00e9mon, they discard Benched Pok\u00e9mon until they have 3 Pok\u00e9mon on the Bench. If more than one effect changes the number of Benched Pok\u00e9mon allowed, use the smaller number.",
            effect=unimplemented,
        ),
        Attack(
            title="Poisonous Gem",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)
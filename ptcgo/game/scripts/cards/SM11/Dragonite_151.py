from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e9c6ae37-5560-504a-ac7c-28f132f36a7f",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=151,
    set_code="SM11",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Hurricane Charge",
            game_text="Once during your turn (before your attack), you may attach a Water Energy card, a Lightning Energy card, or 1 of each from your hand to your Pok\u00e9mon in any way you like.",
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Impact",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=unimplemented,
        ),
    ],
)
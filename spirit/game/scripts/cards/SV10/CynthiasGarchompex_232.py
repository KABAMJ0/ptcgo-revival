from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="afc36acc-fb87-50a3-a755-51763b27b912",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGarchompex.Name",
    display_name="Cynthia's Garchomp ex",
    searchable_by=["Cynthia's Garchomp ex", "Stage 2", "ex", "CynthiasGarchompex"],
    subtypes=["Stage 2", "ex"],
    collector_number=232,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasGabite.Name",
    family_id=443,
    abilities=[
        Attack(
            title="Corkscrew Dive",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=100,
            effect=unimplemented,
        ),
        Attack(
            title="Draconic Buster",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=260,
            effect=unimplemented,
        ),
    ],
)
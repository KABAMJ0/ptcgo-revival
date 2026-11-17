from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6a449e57-33e9-5b1a-9f8e-d8299808fafd",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1", "Electivire"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=125,
    abilities=[
        Attack(
            title="Electroslug",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
        ),
        Attack(
            title="Unleash Lightning",
            game_text="During your next turn, your Pok\u00e9mon can't attack. (This includes new Pok\u00e9mon that come into play.)",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=220,
            effect=unimplemented,
        ),
    ],
)
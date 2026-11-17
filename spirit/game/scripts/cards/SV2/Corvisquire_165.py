from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1fac6266-7fb4-5976-a850-e6e3882a98c2",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corvisquire.Name",
    display_name="Corvisquire",
    searchable_by=["Corvisquire", "Stage 1", "Corvisquire"],
    subtypes=["Stage 1"],
    collector_number=165,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rookidee.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Glide",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=unimplemented,
        ),
    ],
)
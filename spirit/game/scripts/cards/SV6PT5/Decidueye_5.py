from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="03fff42c-724a-58e0-b543-f155601187cf",
    key="SV6PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Decidueye.Name",
    display_name="Decidueye",
    searchable_by=["Decidueye", "Stage 2", "Decidueye"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="SV6PT5",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Attack(
            title="Stock Up on Feathers",
            game_text="Draw cards until you have 7 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Power Shot",
            game_text="Discard a Basic Grass Energy card from your hand. If you can't, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=170,
            effect=unimplemented,
        ),
    ],
)
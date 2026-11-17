from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4d0771bd-0d12-5569-ad70-89b54168b209",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blazikenex.Name",
    display_name="Blaziken ex",
    searchable_by=["Blaziken ex", "Stage 2", "ex", "Blazikenex"],
    subtypes=["Stage 2", "ex"],
    collector_number=24,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Ability(
            title="Seething Spirit",
            game_text="Once during your turn, you may attach a Basic Energy card from your discard pile to 1 of your Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Smolder-sault",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)
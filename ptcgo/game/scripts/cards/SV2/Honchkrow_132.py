from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ba865c81-7519-557e-a1a6-c31c3e16620a",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow", "Stage 1", "Honchkrow"],
    subtypes=["Stage 1"],
    collector_number=132,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Attack(
            title="Flap",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
        ),
        Attack(
            title="Dirty Throw",
            game_text="Discard a card from your hand. If you can't, this attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)
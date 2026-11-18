from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dcb84769-68c8-5212-9964-36487742bf27",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alcremie.Name",
    display_name="Alcremie",
    searchable_by=["Alcremie", "Stage 1", "Alcremie"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SWSH9TG",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    family_id=869,
    abilities=[
        Ability(
            title="Additional Order",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, your turn does not end when you use Caf\u00e9 Master.",
            effect=unimplemented,
        ),
        Attack(
            title="Rainbow Flavor",
            game_text="This attack does 40 more damage for each type of basic Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
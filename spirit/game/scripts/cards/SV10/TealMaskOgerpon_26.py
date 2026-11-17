from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c9188ad1-8c26-5630-8f0a-4355fb28b12f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TealMaskOgerpon.Name",
    display_name="Teal Mask Ogerpon",
    searchable_by=["Teal Mask Ogerpon", "Basic", "TealMaskOgerpon"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1017,
    abilities=[
        Attack(
            title="Grass Kagura",
            game_text="Search your deck for a Basic Grass Energy card and attach it to 1 of your Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Ogre's Hammer",
            game_text="During your next turn, this Pok\u00e9mon can't use Ogre's Hammer.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)
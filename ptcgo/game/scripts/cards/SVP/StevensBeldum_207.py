from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="83597c2c-c162-557c-a920-88fc7fc0096d",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensBeldum.Name",
    display_name="Steven's Beldum",
    searchable_by=["Steven's Beldum", "Basic", "StevensBeldum"],
    subtypes=["Basic"],
    collector_number=207,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=374,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
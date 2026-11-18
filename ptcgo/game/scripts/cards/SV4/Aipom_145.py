from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.card_effects.support_common import draw_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4097cefb-6d36-5501-88a9-dd2c154e4b5d",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=["Aipom", "Basic", "Aipom"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=190,
    abilities=[
        Attack(
            title="Filch",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(1),
        ),
        Attack(
            title="Smack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
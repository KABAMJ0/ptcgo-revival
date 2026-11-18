from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="a94baaf7-0251-52bf-9bcb-e978a80d7033",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name",
    display_name="Dewpider",
    searchable_by=["Dewpider", "Basic", "Dewpider"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=751,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Spider Web",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            effect=no_retreat_attack(),
        ),
    ],
)
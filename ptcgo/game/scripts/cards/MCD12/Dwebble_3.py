from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="6cb771de-0e6e-5027-aaea-9ff0f6f1b776",
    key="MCD12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    display_name="Dwebble",
    searchable_by=["Dwebble", "Basic", "Dwebble"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="MCD12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=557,
    abilities=[
        Attack(
            title="Withdraw",
            game_text="Flip a coin. If heads, prevent all damage done to this Pok\u00e9mon by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_protection(prevent=True),
        ),
        Attack(
            title="Slash",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
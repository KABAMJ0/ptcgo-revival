from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2a1b17ff-3305-54bc-bac6-26759674b049",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name",
    display_name="Flabébé",
    searchable_by=["Flab\u00e9b\u00e9", "Basic", "Flabb"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=669,
    abilities=[
        Attack(
            title="Bind Wound",
            game_text="Heal 30 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Fairy Wind",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
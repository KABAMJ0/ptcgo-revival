from ptcgo.game.card_effects.passives_common import item_or_supporter_effect_shield
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="72fe3440-9ab2-5893-9384-16f1f2624442",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    display_name="Axew",
    searchable_by=["Axew", "Basic", "Axew"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=610,
    abilities=[
        Ability(
            title="Unnerve",
            game_text="Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pok\u00e9mon.",
            passive=item_or_supporter_effect_shield(),
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.METAL: 1},
            damage=20,
        ),
    ],
)
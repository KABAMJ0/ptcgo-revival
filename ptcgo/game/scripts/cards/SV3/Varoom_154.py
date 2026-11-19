from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="3f867b88-8b5b-517e-a55c-117f7eb1c645",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    display_name="Varoom",
    searchable_by=["Varoom", "Basic", "Varoom"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=965,
    abilities=[
        Attack(
            title="Spinning Draw",
            game_text="Draw a card.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=draw_attack(1),
        ),
    ],
)
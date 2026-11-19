from ptcgo.game.card_effects.support_common import discard_then_draw
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import discard_then_draw
card = PokemonCardDef(
    guid="da42868f-84ae-57d5-9676-98dd846c627a",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic", "Klefki"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=707,
    abilities=[
        Attack(
            title="Stick 'n' Draw",
            game_text="Discard a card from your hand. If you do, draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=discard_then_draw(1, 2, optional=True),
        ),
        Attack(
            title="Hook",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
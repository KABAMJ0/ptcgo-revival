from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="726aa4ca-4527-5570-a337-50fe11bb7df7",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    display_name="Tinkatink",
    searchable_by=["Tinkatink", "Basic", "Tinkatink"],
    subtypes=["Basic"],
    collector_number=100,
    set_code="SV2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=957,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw a card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(1),
        ),
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="68bd2876-f871-5589-9ab5-8dd9ede8411a",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name",
    display_name="Tandemaus",
    searchable_by=["Tandemaus", "Basic", "Tandemaus"],
    subtypes=["Basic"],
    collector_number=209,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=924,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(2),
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
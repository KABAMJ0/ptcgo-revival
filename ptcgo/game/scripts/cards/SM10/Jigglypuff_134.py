from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="e606ae73-463e-5dea-be0d-4772f80d2b5d",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    display_name="Jigglypuff",
    searchable_by=["Jigglypuff", "Basic", "Jigglypuff"],
    subtypes=["Basic"],
    collector_number=134,
    set_code="SM10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=39,
    abilities=[
        Attack(
            title="Ball Roll",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(per_heads=20, until_tails=True),
        ),
    ],
)
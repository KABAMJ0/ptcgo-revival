from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="3ddb2821-fe2b-58e0-adee-b5b3841604d8",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name",
    display_name="Mudbray",
    searchable_by=["Mudbray", "Basic", "Mudbray"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=749,
    abilities=[
        Attack(
            title="Running Charge",
            game_text="Flip a coin until you get tails. This attack does 40 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=flip_damage(per_heads=40, until_tails=True),
        ),
    ],
)
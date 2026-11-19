from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="a99e266b-95f8-5557-b9e7-ed83455b3cf3",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    display_name="Marill",
    searchable_by=["Marill", "Basic", "Marill"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=183,
    abilities=[
        Attack(
            title="Ball Roll",
            game_text="Flip a coin until you get tails. This attack does 10 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(per_heads=10, until_tails=True),
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
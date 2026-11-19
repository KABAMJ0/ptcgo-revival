from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import flip_damage
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="3b64a689-9302-5a1d-aaaa-0786815456e6",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gimmighoul.Name",
    display_name="Gimmighoul",
    searchable_by=["Gimmighoul", "Basic", "Gimmighoul"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=999,
    abilities=[
        Attack(
            title="Continuous Coin Toss",
            game_text="Flip a coin until you get tails. This attack does 20 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(per_heads=20, until_tails=True),
        ),
    ],
)
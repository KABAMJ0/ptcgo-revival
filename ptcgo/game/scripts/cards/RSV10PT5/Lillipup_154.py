from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_bonus

card = PokemonCardDef(
    guid="6537b13f-93ca-58b7-b57a-2362dc4fc24f",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name",
    display_name="Lillipup",
    searchable_by=["Lillipup", "Basic", "Lillipup"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=506,
    abilities=[
        Attack(
            title="Play Rough",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
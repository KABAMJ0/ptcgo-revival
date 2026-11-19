from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, count_energy

card = PokemonCardDef(
    guid="c3ac3921-02c1-520e-8793-eaa2b934488a",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    display_name="Tynamo",
    searchable_by=["Tynamo", "Basic", "Tynamo"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=602,
    abilities=[
        Attack(
            title="Aqua Shock",
            game_text="If your opponent's Active Pok\u00e9mon has any Water Energy attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(lambda ctx: count_energy("defender", PokemonTypes.WATER)(ctx) > 0, 30),
        ),
    ],
)
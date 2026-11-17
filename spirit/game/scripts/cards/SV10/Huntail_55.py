from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="83b30ed9-84fd-5bd7-bb31-8a3464ed5bb3",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Huntail.Name",
    display_name="Huntail",
    searchable_by=["Huntail", "Stage 1", "Huntail"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    family_id=366,
    abilities=[
        Ability(
            title="Diver's Catch",
            game_text="When 1 of your Water Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, you may put all Basic Water Energy attached to that Pok\u00e9mon into your hand instead of the discard pile.",
            effect=unimplemented,
        ),
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="00e11946-e495-51ca-9eb8-17fa8fab3155",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiramex.Name",
    display_name="Reshiram ex",
    searchable_by=["Reshiram ex", "Basic", "ex", "Reshiramex"],
    subtypes=["Basic", "ex"],
    collector_number=173,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Blazing Burst",
            game_text="This attack does 50 more damage for each Prize card your opponent has taken. Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
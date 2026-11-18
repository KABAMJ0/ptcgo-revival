from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9cd91944-3a44-5cac-b473-e793f2c89dcc",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidonex.Name",
    display_name="Koraidon ex",
    searchable_by=["Koraidon ex", "Basic", "ex", "Koraidonex"],
    subtypes=["Basic", "ex"],
    collector_number=197,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    abilities=[
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Revenge Buster",
            game_text="If your Benched Pok\u00e9mon have any damage counters on them, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
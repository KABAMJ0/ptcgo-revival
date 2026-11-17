from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="30b5f077-2db8-5ea4-a7d0-735617e53628",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMuk.Name",
    display_name="Alolan Muk",
    searchable_by=["Alolan Muk", "Stage 1", "AlolanMuk"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Power of Alchemy",
            game_text="Each Basic Pok\u00e9mon in play, in each player's hand, and in each player's discard pile has no Abilities.",
            effect=unimplemented,
        ),
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=unimplemented,
        ),
    ],
)
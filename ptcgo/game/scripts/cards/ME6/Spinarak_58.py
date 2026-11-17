from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="72fa11ce-1956-5fd7-83ec-f73f77948175",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    display_name="Spinarak",
    searchable_by=["Spinarak", "Basic", "Spinarak"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="ME6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=167,
    abilities=[
        Attack(
            title="Poison Sting",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Bug Out",
            game_text="Reveal the bottom 7 cards of your deck, and this attack does 50 damage for each Pok\u00e9mon you find there that has the Bug Out attack. Then, shuffle any revealed Pok\u00e9mon back into your deck. Discard the other cards.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
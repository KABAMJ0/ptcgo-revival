from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cbd96e7c-c802-5d0f-ab7c-ecb1db252a77",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roggenrola.Name",
    display_name="Roggenrola",
    searchable_by=["Roggenrola", "Basic", "Roggenrola"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="RSV10PT5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=524,
    abilities=[
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks if that damage is 40 or less.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=protect_next_turn(prevent=True, max_damage=40),
        ),
        Attack(
            title="Rolling Rocks",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
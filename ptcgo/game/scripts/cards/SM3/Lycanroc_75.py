from ptcgo.game.session.effects import is_basic_pokemon
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack, active_is, bonus_if

card = PokemonCardDef(
    guid="4c13e677-143f-51aa-a4c9-e6687f7a3b22",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lycanroc.Name",
    display_name="Lycanroc",
    searchable_by=["Lycanroc", "Stage 1", "Lycanroc"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=745,
    abilities=[
        Attack(
            title="Dangerous Claws",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=bonus_if(active_is(is_basic_pokemon), 30),
        ),
        Attack(
            title="Corner",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=no_retreat_attack(),
        ),
    ],
)
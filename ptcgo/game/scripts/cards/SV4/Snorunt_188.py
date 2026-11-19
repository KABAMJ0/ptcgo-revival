from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import pokemon_of_types
from ptcgo.game.card_effects.attacks_common import bonus_if, active_is


card = PokemonCardDef(
    guid="d7c2ec60-c2db-5960-a006-3bc5bde5ba72",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    display_name="Snorunt",
    searchable_by=["Snorunt", "Basic", "Snorunt"],
    subtypes=["Basic"],
    collector_number=188,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=361,
    abilities=[
        Attack(
            title="Ice Shard",
            game_text="If your opponent's Active Pok\u00e9mon is a Fighting Pok\u00e9mon, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(active_is(pokemon_of_types(PokemonTypes.FIGHTING)), 30),
        ),
    ],
)
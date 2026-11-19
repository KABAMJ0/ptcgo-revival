from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import pokemon_of_types
from ptcgo.game.card_effects.attacks_common import bonus_if, active_is


card = PokemonCardDef(
    guid="7d6a12dd-53ae-58b1-9bce-cd4df15b94ae",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    display_name="Snover",
    searchable_by=["Snover", "Basic", "Snover"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=459,
    abilities=[
        Attack(
            title="Ice Shard",
            game_text="If your opponent's Active Pok\u00e9mon is a Fighting Pok\u00e9mon, this attack does 40 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(active_is(pokemon_of_types(PokemonTypes.FIGHTING)), 40),
        ),
    ],
)
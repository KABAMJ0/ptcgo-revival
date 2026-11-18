from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import evolution_lock_passive

card = PokemonCardDef(
    guid="a13d358a-1bfe-5f9f-a091-adbf9cc429f2",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=483,
    abilities=[
        Ability(
            title="Time Aura",
            game_text="As long as Dialga is your Active Pok\u00e9mon, your opponent can't play any Pok\u00e9mon from his or her hand to evolve his or her Active Pok\u00e9mon.",
            passive=evolution_lock_passive(active_only=True),
        ),
        Attack(
            title="Metal Burn",
            game_text="Discard all Metal Energy attached to Dialga.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)
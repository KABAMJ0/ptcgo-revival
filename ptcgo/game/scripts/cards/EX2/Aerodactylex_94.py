from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="a9206eab-9c75-5eb7-9e28-8adacb1d49e8",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aerodactylex.Name",
    display_name="Aerodactyl ex",
    searchable_by=["Aerodactyl ex", "Stage 1", "ex", "Aerodactylex"],
    subtypes=["Stage 1", "ex"],
    collector_number=94,
    set_code="EX2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=142,
    abilities=[
        Ability(
            title="Primal Lock",
            game_text="As long as Aerodactyl ex is in play, your opponent can't play Pok\u00e9mon Tool cards. Remove any Pok\u00e9mon Tool cards attached to your opponent's Pok\u00e9mon and put them into his or her discard pile.",
            effect=unimplemented,
        ),
        Attack(
            title="Supersonic",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
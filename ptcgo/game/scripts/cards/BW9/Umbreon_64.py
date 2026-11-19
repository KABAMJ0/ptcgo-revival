from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import team_hp_bonus
from ptcgo.game.card_effects.pokemon import has_pokemon_subtype

card = PokemonCardDef(
    guid="187da285-36e6-5ca6-a3bb-7b34e7efaad0",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1", "Team Plasma", "Umbreon"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=64,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Dark Shade",
            game_text="Each of your Team Plasma Pok\u00e9mon in play gets +20 HP.",
            passive=team_hp_bonus(20, protects="team", pred=lambda pokemon, carrier: (
                has_pokemon_subtype(pokemon, "Team Plasma"))),
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
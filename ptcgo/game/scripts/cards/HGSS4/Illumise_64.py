from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_in_play, flip_damage
from ptcgo.game.card_effects.energies import pokemon_named_like

card = PokemonCardDef(
    guid="1a8d55aa-aca3-518e-8cf7-defeca90c2bd",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name",
    display_name="Illumise",
    searchable_by=["Illumise", "Basic", "Illumise"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=314,
    abilities=[
        Attack(
            title="Sweet Scent",
            game_text="Remove 3 damage counters from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Vulcan Beat",
            game_text="Flip a coin for each Volbeat you have in play. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins_from=count_in_play("mine", pokemon_named_like("Volbeat")), per_heads=30),
        ),
    ],
)